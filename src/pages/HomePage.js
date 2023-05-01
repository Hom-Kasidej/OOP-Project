import React from "react";
import "./home-page.css"
import ResponsiveAppBar from '../components/AppBar';
import { Component,useState } from 'react';
import SelectVariants from "../components/Select";
import {FirstComponent,SecondComponent} from "../components/datepickers";
import SearchButton from "../components/Button_search";
import CarTypeCard from "../components/CarTypeCard";
import { Grid, InputLabel } from "@mui/material";


function Home() {
    const byCarType = [{
        type : 'Eco Car',
        img : './IMG/3209935.png'
    },
    {
        type : 'Sedan',
        img : '../../IMG/2736918.png'
    },
    {
        type : 'SUV',
        img : '../../IMG/55280.png'
    }
    ,
    {
        type : 'Van',
        img : '../../IMG/335004.png'
    }
    ,
    {
        type : 'Luxury',
        img : '../../IMG/640173.png'
    }]
    const token = localStorage.getItem('accessToken');
    const [authorized, setAuthorized] = useState(false);
    const handleLogOut = () => {
        localStorage.removeItem('accessToken');
        window.location.href = '/';
    }
    return (
        <div className="search-page">
            
            
            
            
            <Grid container padding={15} justifyContent='space-between' >
                <Grid item> <SelectVariants > </SelectVariants> </Grid>
                <Grid item> <FirstComponent > </FirstComponent> </Grid>
                <Grid item> <SecondComponent> </SecondComponent> </Grid>
                <Grid item> <SearchButton> </SearchButton> </Grid>
            </Grid>
                
                
            <p style = {{color : 'white', textAlign: 'center', fontSize: '40px',backgroundColor: 'rgba(0, 0, 0, 0.3)'}}>ค้นหารถเช่าตามประเภท</p>
                
            
            <Grid container padding={15} justifyContent='space-evenly'>
                {byCarType.map((carType) => <Grid item><CarTypeCard type = {carType.type} img = {carType.img}/></Grid> )}
            </Grid>
                    
                    
        </div>
    )
}

export default Home;