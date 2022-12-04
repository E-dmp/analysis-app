import axios from 'axios'
import { useState } from 'react'
import { nanoid } from 'nanoid'
import reactStringReplace from 'react-string-replace'
import {
  VerticalTimeline,
  VerticalTimelineElement,
} from 'react-vertical-timeline-component'
import 'react-vertical-timeline-component/style.min.css'

const TWEET_URL = 'https://twitter.com/'

type Tweet = {
  TweetData: Array<string>
}


function App () {
  const [data, setTweetData] = useState<Tweet>()
  const url = 'http://127.0.0.1:8000'

  const getTweetData = () => {
    axios.get(url).then((res) => {
      setTweetData(res.data.TweetData)
      console.log(res.data.TweetData)
    })
  }
  return (
    <div>
      <div className="centerTitle">
        <h1>
        KeyWord-TimeLine
        </h1>
      </div>
      <div>
        {data ? (
          <div>
            <VerticalTimeline>
              {Object.values(data).map((tweet: any) => (
                <VerticalTimelineElement
                  key={nanoid()}
                  className='vertical-timeline-element--work'
                  
                  contentStyle={{
                    background: 'rgb(255, 255, 255)',
                    color: '#fff',
                  }}
                  contentArrowStyle={{
                    borderRight: '14px solid rgb(178, 224, 220)',
                  }}
                  
                  date={tweet.created_at}
                  iconStyle={{ background: 'rgb(178, 224, 220)', color: '#dc5353' }}
                >
                  {reactStringReplace(
                    TWEET_URL,
                    /(https?:\/\/\S+)/g,
                    (match, i) => (
                      <div className='container'>

                      <a key={i} href={match + tweet.name + "/status/"+ tweet.id} target='_blank' className='linkWrap'>
                        <div className='cardHeader'>
                        <img src={tweet.profile_image_url} alt="" className='userIcon'/>
                        <h3 className='userName'>{tweet.name}</h3>
                        </div>
                        <h4 className='twText'>{tweet.text}</h4>
                        {tweet.media_url ? (<img src={tweet.media_url} alt="" className='mediaImages'/>):(<div></div>)}
                        
                      </a>
                      </div>
                    )
                  )}
                </VerticalTimelineElement>
              ))}
            </VerticalTimeline>
          </div>
        ) : (
          <div className='button-wrapper'><button onClick={getTweetData} className="button">データを取得</button></div>
        )}
      </div>
    </div>
  )
}

export default App
