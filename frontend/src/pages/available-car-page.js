import { Box, Grid } from '@mui/material';
import './available-car-page.css';

//import {cars} from '../db/cars'
import MultiActionAreaCard from '../components/car-card';
import axios from 'axios';
import { useEffect, useState} from 'react';


function Cars() {
  const [availableCars,setCars] = useState([]);
  useEffect(() => {
    const endpoint = "http://127.0.0.1:7000/Car"
    axios.get(endpoint).then((response) => { 
      
      console.log(response.data);
      setCars(response.data.Cars);
    })
  });
  
  return (
    <div className='car-display'>
      <Box>
        <Grid container padding={10} justifyContent='space-between' rowSpacing={{ xs: 1, sm: 2, md: 3 }}>
        {availableCars.map((car) => <Grid item>
                              <MultiActionAreaCard 
                                              img = {car._Car__images}
                                              name = {car._Car__brand + " " + car._Car__color}
                                              loc = {car._Car__location}
                                              pricePerDay = {car._Car__price}
                                              carType = {car._Car__type}
                                              gearType = {car._Car__gear_type}
                                              distance = {car._Car__distance}
                                              features = {car._Car__features}
                                              gps = {car._Car__gps_type}
                                              fuelType = {car._Car__fuel_type}
                                              seats = {car._Car__seats} /></Grid>)}
                                            
        </Grid>
      </Box>
      
      
    </div>
  );
}

export default  Cars;