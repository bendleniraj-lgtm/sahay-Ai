import { useState } from 'react'

export default function App() {
  const [message, setMessage] = useState('')
  const [reply, setReply] = useState('')
  const [loading, setLoading] = useState(false)

  const handleSubmit = async (event) => {
    event.preventDefault()
    setLoading(true)
    setReply('')

    try {
      const response = await fetch('http://localhost:8000/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message })
      })

      const data = await response.json()
      setReply(data.reply)
    } catch (error) {
      setReply('Unable to reach the backend server.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app-shell">
      <div className="card">
        <h1>Sahay AI</h1>
        <p>Ask the assistant anything.</p>

        <form onSubmit={handleSubmit}>
          <textarea
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Type your message here..."
            rows="5"
          />
          <button type="submit" disabled={loading || !message.trim()}>
            {loading ? 'Sending...' : 'Send'}
          </button>
        </form>

        {reply && (
          <div className="reply-box">
            <strong>Reply:</strong>
            <p>{reply}</p>
          </div>
        )}
      </div>
    </div>
  )
}
