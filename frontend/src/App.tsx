import axios from 'axios'
import { useState } from 'react'
import { nanoid } from 'nanoid'
import {
  VerticalTimeline,
  VerticalTimelineElement,
} from 'react-vertical-timeline-component'
import 'react-vertical-timeline-component/style.min.css'
type Tweet = {
  TweetData: Array<string>
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
          <div>
            <VerticalTimeline>
            {data.TweetData.map((twdata) => (
                <VerticalTimelineElement
                  key={nanoid()}
                  className='vertical-timeline-element--work'
                  contentStyle={{
                    background: 'rgb(33, 150, 243)',
                    color: '#fff',
                  }}
                  contentArrowStyle={{
                    borderRight: '7px solid  rgb(33, 150, 243)',
                  }}
                  date='2011 - present'
                  iconStyle={{ background: 'rgb(33, 150, 243)', color: '#fff' }}
                >
                  <h3 className='vertical-timeline-element-title'>{twdata}</h3>
                </VerticalTimelineElement>
                
                ))}
                </VerticalTimeline>
          </div>
        ) : (
          <button onClick={getTweetData}>データを取得</button>
        )}
      </div>
    </div>
  )
}

export default App
