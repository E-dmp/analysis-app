import axios from 'axios'
import { useState } from 'react'

type Sample = {
  Hello: string
}

function App () {
  const [data, setData] = useState<Sample>()
  const url = 'http://127.0.0.1:8000'

  const getTweetData = () => {
    axios.get(url).then((res) => {
      setData(res.data)
      console.log(res.data)
    })
  }
  return (
    <div>
      <div>感情分析アプリ</div>
      <div>
        {data ? (
          <div>{data.Hello}</div>
        ) : (
          <button onClick={getTweetData}>データを取得</button>
        )}
      </div>
    </div>
  )
}

export default App
