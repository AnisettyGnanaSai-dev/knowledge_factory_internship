"use client";

import { useState } from "react";
import { getCurrentUser } from "../../lib/supabase";

export default function TestPage() {
  const [result, setResult] = useState("");

  async function testConnection() {
    const user = await getCurrentUser();

    console.log(user);

    setResult(JSON.stringify(user, null, 2));
  }

  return (
    <div>
      <h1>Supabase Test</h1>

      <button onClick={testConnection}>
        Test Connection
      </button>

      <pre>{result}</pre>
    </div>
  );
}