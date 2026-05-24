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
