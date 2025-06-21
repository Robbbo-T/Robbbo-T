import { useState } from 'react';
import axios from 'axios';

export default function Home() {
  const [file, setFile] = useState(null);
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async () => {
    if (!file) return;

    setLoading(true);
    setResults(null);
    setError(null);

    const formData = new FormData();
    formData.append('file', file);

    try {
      const res = await axios.post('http://localhost:8000/run-zip/', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      setResults(res.data);
    } catch (err) {
      setError(err.response?.data.detail || err.message);
    }

    setLoading(false);
  };

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-4">ZIP Interpreter & Tester</h1>
      <input
        type="file"
        accept=".zip"
        onChange={(e) => setFile(e.target.files[0])}
        className="mb-4"
      />
      <button
        onClick={handleSubmit}
        disabled={!file || loading}
        className="px-4 py-2 bg-blue-500 text-white rounded disabled:opacity-50"
      >
        {loading ? 'Running...' : 'Upload & Run'}
      </button>

      {error && <div className="text-red-500 mt-4">Error: {error}</div>}

      {results && (
        <div className="mt-4">
          {Object.entries(results).map(([filename, res]) => (
            <div key={filename} className="border-b pb-2 mb-2">
              <h3 className="font-semibold">{filename}</h3>
              {res.test_file && <span className="text-sm text-green-500">(Test file)</span>}
              {res.error && <div className="text-red-500">Error: {res.error}</div>}
              {res.stdout && (
                <div>
                  <strong>Output:</strong>
                  <pre className="bg-gray-100 p-2 rounded">{res.stdout}</pre>
                </div>
              )}
              {res.stderr && (
                <div>
                  <strong>Errors:</strong>
                  <pre className="bg-gray-100 p-2 rounded text-red-500">{res.stderr}</pre>
                </div>
              )}
              <div>
                <strong>Return code:</strong> {res.returncode}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
