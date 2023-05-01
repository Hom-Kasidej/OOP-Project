import * as React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { Button, CardActionArea, CardActions } from '@mui/material';

export default function MultiActionAreaCard(props) {
  return (
    <Card sx={{ width: 400, height: 550 }}>
        <CardMedia
          component="img"
          height="300"
          image= {props.img[0]}
          alt="car for rent "
          sx={{objectFit : "contain"}}
        />
        <CardContent>
          <Typography gutterBottom variant="h6" component="div">
            {props.name}
          </Typography>
          <Typography variant="body2" color="text.secondary">
            <ul>
                <li>Location : {props.loc}</li>
                <li>Car Type : {props.carType}</li>
                <li>Gear Type : {props.gearType}</li>
                <li>Distance : {props.distance}</li>
                <li>Features : {props.features}</li>
                <li>GPS type : {props.gps}</li>
                <li>Fuel type : {props.fuelType}</li>
                <li>Seats : {props.seats}</li>
            </ul>
            <h1>{props.pricePerDay} THB/day</h1>
          </Typography>
        </CardContent>
      <CardActions>
        <Button size="small" color="primary">
          จองตอนนี้
        </Button>
      </CardActions>
    </Card>
  );
}