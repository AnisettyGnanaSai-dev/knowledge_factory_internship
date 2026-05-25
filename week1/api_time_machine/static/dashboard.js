async function loadHistory() {

    let response = await fetch("/history")

    let data = await response.json()

    let container = document.getElementById("history-container")

    container.innerHTML = ""

    data.forEach(item => {

        container.innerHTML += `

        <div class="card">

            <h3>${item.endpoint}</h3>

            <p><b>Method:</b> ${item.method}</p>

            <p><b>Status:</b> ${item.status_code}</p>

            <pre>${JSON.stringify(item.request_body, null, 2)}</pre>

            <button onclick="analyzeRequest('${item._id}')">
                AI Analyze
            </button>

            <button onclick="replayRequest('${item._id}')">
                Replay
            </button>

        </div>
        `
    })
}


// updated by codex: dashboard UI flow for testing external APIs with selectable HTTP method
async function testExternalApi() {

    const method = document.getElementById("method-select").value
    const url = document.getElementById("url-input").value.trim()
    const rawBody = document.getElementById("body-input").value.trim()

    if (!url) {
        alert("Please enter a URL")
        return
    }

    let requestBody = null
    if (rawBody) {
        try {
            requestBody = JSON.parse(rawBody)
        } catch (error) {
            alert("Body must be valid JSON")
            return
        }
    }

    const response = await fetch("/test-external", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            method,
            url,
            request_body: requestBody
        })
    })

    const data = await response.json()

    if (!response.ok) {
        alert(data.error || "Failed to test API")
        return
    }

    alert(`Saved response with status ${data.status_code}`)
    loadHistory()
}


async function analyzeRequest(id) {

    // updated by codex: show user-visible loading state while AI call is in progress
    alert("AI is thinking... Please wait.")

    try {

        let response = await fetch(`/analyze/${id}`)

        let data = await response.json()

        if (!response.ok) {
            alert(data.error || "AI analysis failed.")
            return
        }

        if (!data.analysis) {
            alert("AI returned no analysis. Check Ollama service/model and try again.")
            return
        }

        alert(data.analysis)

    } catch (error) {

        alert("AI analyze request failed. Please check backend and Ollama server.")
    }
}


async function replayRequest(id) {

    let response = await fetch(`/replay/${id}`)

    let data = await response.json()

    alert(JSON.stringify(data, null, 2))
}
