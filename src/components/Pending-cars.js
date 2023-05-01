import React from 'react';
import './pending-cars.css';
import { useState } from 'react';

function PendingCars() {
  const [pendingCars, setPendingCars] = useState([
    { id: 1, name: 'Car 1', status: 'Pending' },
    { id: 2, name: 'Car 2', status: 'Pending' },
    { id: 3, name: 'Car 3', status: 'Pending' }
  ]);

  const [availableCars, setAvailableCars] = useState([
    { id: 4, name: 'Car 4', status: 'Available' },
    { id: 5, name: 'Car 5', status: 'Available' },
    { id: 6, name: 'Car 6', status: 'Available' }
  ]);

  const [successCars, setSuccessCars] = useState([]);

  const handleVerify = (id) => {
    const updatedCars = pendingCars.filter((car) => car.id !== id);
    const verifiedCar = pendingCars.find((car) => car.id === id);
    verifiedCar.status = 'Success';
    if (verifiedCar.status === 'Success') {
      setSuccessCars([...successCars, verifiedCar]);
    } else {
      setAvailableCars([...availableCars, verifiedCar]);
    }
    setPendingCars(updatedCars);
  };

  const handleDelete = (id) => {
    const updatedCars = availableCars.filter((car) => car.id !== id);
    setAvailableCars(updatedCars);
  };

  return (
    <div className="container">
      <div className="section">
        <h2>Pending Cars</h2>
        {pendingCars.map((car) => (
          <div className="card" key={car.id}>
            <h3>{car.name}</h3>
            <p>Status: {car.status}</p>
            <button className="btn" onClick={() => handleVerify(car.id)}>Verify</button>
          </div>
        ))}
      </div>
      <div className="section">
        <h2>Available Cars</h2>
        {availableCars.map((car) => (
          <div className="card" key={car.id}>
            <h3>{car.name}</h3>
            <p>Status: {car.status}</p>
            <button className="btn delete" onClick={() => handleDelete(car.id)}>Delete</button>
          </div>
        ))}
      </div>
      <div className="section">
        <h2>Success Cars</h2>
        {successCars.map((car) => (
          <div className="card" key={car.id}>
            <h3>{car.name}</h3>
            <p>Status: {car.status}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default PendingCars;