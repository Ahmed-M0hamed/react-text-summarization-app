import logo from './logo.svg';
import './App.css';
import {useState } from 'react'
import axios from 'axios'

function App() {
  const [passage , setPassage] = useState('')
  const [summary , setSummary] = useState(null)
  const handleChange = (e) => {
    const text = e.target.value 
    setPassage(text)
  }
  const handleCLick = () => {
    const data  = {
      'text' : passage ,
    }
    axios.post('http://localhost:8000/predict/' , data)
    .then(res => setSummary(res.data)) 
  }
  return (
    <div className="App">
      <header className="App-header">
        <h2>text summarization</h2>
        <textarea value={passage} onChange={handleChange}></textarea>
        <button type='submit' onClick={handleCLick}>summarize</button>
        {summary && <p>{summary}</p>}
        
      </header>
    </div>
  );
}

export default App;
