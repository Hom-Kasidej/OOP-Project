import react, { useState, createContext } from 'react'

export const CarContext = createContext();

export const CarProvider = (props) => {
    const [cars, setCars] = useState({ "car" : [] });

    return(
        <CarContext.Provider>
            {props.children}
        </CarContext.Provider>
    );
}