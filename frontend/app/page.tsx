"use client";

import { useState } from "react";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
} from "recharts";

export default function Home() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!query) return;

    setLoading(true);
    const res = await fetch("/api/query", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ query }),
    });

    const data = await res.json();
    setResponse(data);
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 to-black text-white flex flex-col items-center p-6">

      {/* Header */}
      <div className="w-full max-w-3xl text-center mb-6">
        <h1 className="text-4xl font-bold tracking-tight">
          SupaChat 🚀
        </h1>
        <p className="text-gray-400 mt-2">
          Ask your database in plain English
        </p>
      </div>

      {/* Chat Card */}
      <div className="w-full max-w-3xl bg-gray-800/70 backdrop-blur-lg p-6 rounded-2xl shadow-xl border border-gray-700">

        {/* Input */}
        <div className="flex gap-2">
          <input
            className="flex-1 p-3 rounded-lg bg-gray-900 border border-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="e.g. Show top trending topics"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />

          <button
            onClick={handleSend}
            className="bg-blue-600 hover:bg-blue-700 transition px-4 py-2 rounded-lg font-medium"
          >
            {loading ? "..." : "Send"}
          </button>
        </div>

        {/* Response */}
        <div className="mt-6">
          {loading && (
            <p className="text-gray-400">Fetching insights...</p>
          )}

          {response && (
            <div className="bg-black/40 p-4 rounded-lg border border-gray-700">

              {/* Chat Message */}
              <p className="text-green-400 mb-3">
                ✅ Showing results for: "{response.query}"
              </p>

              {/* Table */}
              <table className="w-full text-left border border-gray-700">
                <thead>
                  <tr className="border-b border-gray-700">
                    {Object.keys(response.data[0] || {}).map((key) => (
                      <th key={key} className="p-2 capitalize">
                        {key}
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {response.data.map((row: any, i: number) => (
                    <tr key={i} className="border-b border-gray-800">
                      {Object.values(row).map((val: any, j: number) => (
                        <td key={j} className="p-2">
                          {val}
                        </td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>

              {/* Chart */}
              <div className="mt-6 h-64">
                <p className="text-gray-400 mb-2">📊 Visualization</p>
                <ResponsiveContainer width="100%" height="100%">
                  <BarChart data={response.data}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey={Object.keys(response.data[0])[0]} />
                    <YAxis />
                    <Tooltip />
                    <Bar dataKey={Object.keys(response.data[0])[1]} />
                  </BarChart>
                </ResponsiveContainer>
              </div>

            </div>
          )}
        </div>
      </div>

      {/* Footer */}
      <p className="text-gray-500 text-xs mt-6">
        Built for DevOps Assessment ⚡
      </p>
    </div>
  );
}