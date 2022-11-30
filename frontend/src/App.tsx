import axios from 'axios'
import { useState } from 'react'
import { nanoid } from 'nanoid'

type Tweet = {
  TweetData:any
  text: string
}

function App () {
  const [data, setTweetData] = useState<Tweet>()
  const url = 'http://127.0.0.1:8000'

  const getTweetData = () => {
    axios.get(url).then((res) => {
      setTweetData(res.data)
      console.log(res.data)
    })
  }
  return (
    <div>
      <div>感情分析アプリ</div>
      <div>
        {data ? (
          <div>{data.TweetData.map((twdata: string[]) => (
            <li key={nanoid()}>{twdata}</li>
          ))}</div>
        ) : (
          <button onClick={getTweetData}>データを取得</button>
        )}


      </div>
    </div>
  )
}

export default App
