import React, {useEffect, useState} from 'react';
import axios from "axios";

const App = () => {
    const [pizzas, setPizzas] = useState([])

    useEffect(() => {
        axios.get('/api/pizzas').then(({data}) => {
            return setPizzas(data.data)
        })
    }, []);
    return (
        <div>
            {pizzas.map((pizza) => <div key={pizza.id}>{JSON.stringify(pizza)}</div>)}
        </div>
    );
};

export {App};