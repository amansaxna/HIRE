import React , { useEffect , useState} from 'react';

function Joke() {
    const [joke , setJoke] = useState({});


    //arrow function :: call back function
    //useEffect run on every render 
    useEffect( () => {
        //fetch doe't hinders the execution therefore console.log works first
        fetch('https://official-joke-api.appspot.com/jokes/random')
        .then(response => response.json())
        .then(json => {
            console.log('joke json',json);
            // function(json) =>callback  {return console.log()}
            setJoke(json);
        });
    }, [] ); //[] to limit only when smethings change

    const { setup , punchline} = joke
return (
    <div>
        <h3>
            JOKE
        </h3>
<p>{setup}</p>
<p>{punchline}</p>
    </div>
)

}
export default Joke;