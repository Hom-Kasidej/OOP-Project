import './App.css';

import { BrowserRouter, NavLink, Routes, Route} from 'react-router-dom'
import { Component,useState } from 'react';

import Home from './pages/HomePage'
import SignUp from './pages/SignUp'
import SignIn from './pages/SignInPage';
import ResponsiveAppBar from './components/AppBar';
import Cars from './pages/available-car-page';
import { cars } from './db/cars';
import Car from './pages/car-page';
import Profile from './pages/profile-page'
import HomePageDealer from './pages/HomePage-dealer';
import ProfileDealer from './pages/profile-page-dealer';

import {CarProvider} from './db/carsContext';
import { BottomNavigation } from '@mui/material';

function App() {
  const token = localStorage.getItem('accessToken');
  const [authorized, setAuthorized] = useState(false);
  const handleLogOut = () => {
        localStorage.removeItem('accessToken');
        window.location.href = '/';
    }
  return (
   
      <div>
        <ResponsiveAppBar toChild = {token ? true : false} logOut = {handleLogOut}/>
        <Routes>
          <Route path="/" element={<Home/>}/>
          <Route path="/sign-in" element={<SignIn/>}/>
          <Route path="/sign-up" element={<SignUp/>}/>
          <Route path="/available-cars" element={<Cars/>}/>
          {cars.map((car) => (<Route path={`/car/${car.id}`} element={<Car img = {car.img} 
                                                                           name = {car.label} 
                                                                           loc = {car.loc} 
                                                                           type = {car.type}
                                                                           gearType = {car.gearType}
                                                                           pricePerDay = {car.pricePerDay}/>}/>))}
          <Route path="/profile" element={<Profile/>}/>    
          <Route path="/HFD" element={<HomePageDealer/>}/>
          <Route path="/PFD" element={<ProfileDealer/>}/>                                                   
        </Routes>
         
      </div>
      
  );
}

export default App;
