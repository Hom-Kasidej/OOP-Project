import * as React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { CardActionArea } from '@mui/material';

export default function CarTypeCard(props) {
  return (
    <Card sx={{ width : 200, height : 200}}>
      <CardActionArea>
        <CardMedia
          component="img"
          height="125"
          image={props.img}
          alt="cartype"
          sx = {{objectFit : 'contain'}}
        />
        <CardContent>
          <Typography gutterBottom variant="h5" component="div">
            {props.type}
          </Typography>
          <Typography variant="body2" color="text.secondary">
          </Typography>
        </CardContent>
      </CardActionArea>
    </Card>
  );
}