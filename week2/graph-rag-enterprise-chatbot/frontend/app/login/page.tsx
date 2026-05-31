"use client";

import { useState } from "react";

import {
  signIn,
  getUserRole,
} from "../../lib/supabase";

import { useRouter } from "next/navigation";

export default function LoginPage() {
  const router = useRouter();

  const [email, setEmail] =
    useState("");

  const [password, setPassword] =
    useState("");

  const [error, setError] =
    useState("");

  async function handleLogin(
    e: React.FormEvent
  ) {
    e.preventDefault();

    setError("");

    console.log(
      "LOGIN STARTED"
    );

    const { error } =
      await signIn(
        email,
        password
      );

    if (error) {
      console.log(
        "LOGIN ERROR:",
        error
      );

      setError(
        error.message
      );

      return;
    }

    console.log(
      "LOGIN SUCCESS"
    );

    await new Promise(
      (resolve) =>
        setTimeout(
          resolve,
          2000
        )
    );

    const role =
      await getUserRole();

    console.log(
      "FINAL ROLE:",
      role
    );

    if (role === "admin") {
      console.log(
        "REDIRECTING ADMIN"
      );

      router.push(
        "/dashboard/admin"
      );
    } else if (
      role ===
      "developer"
    ) {
      console.log(
        "REDIRECTING DEVELOPER"
      );

      router.push(
        "/dashboard/developer"
      );
    } else if (
      role === "intern"
    ) {
      console.log(
        "REDIRECTING INTERN"
      );

      router.push(
        "/dashboard/intern"
      );
    } else {
      console.log(
        "REDIRECTING CLIENT"
      );

      router.push(
        "/dashboard/client"
      );
    }
  }

  return (
    <div
      style={{
        width: "400px",
        margin:
          "100px auto",
      }}
    >
      <h1>
        GraphRAG Login
      </h1>

      <form
        onSubmit={
          handleLogin
        }
      >
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) =>
            setEmail(
              e.target.value
            )
          }
        />

        <br />
        <br />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) =>
            setPassword(
              e.target.value
            )
          }
        />

        <br />
        <br />

        <button
          type="submit"
        >
          Login
        </button>
      </form>

      {error && (
        <p
          style={{
            color: "red",
          }}
        >
          {error}
        </p>
      )}
    </div>
  );
}