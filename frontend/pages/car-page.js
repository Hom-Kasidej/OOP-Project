import React from 'react';
import { Box, Typography, Grid, TextField, FormControlLabel, Checkbox, Button } from '@mui/material';
import SelectVariants from '../components/Select';
import { FirstComponent, SecondComponent } from '../components/datepickers';

function Car(props) {
  return (<div>
    <Typography>
      <img src={props.img} />
    </Typography>
    <Grid container sx = {{ justifyContent: 'center'}}>
      <Typography variant='h4'>
      {props.name}
      </Typography>
    </Grid>
    
    <Grid container padding={5} justifyContent='space-between'>
      <Grid item>
        <Box sx={{
          margin: 'auto',
          flexDirection: 'row-reverse',
          width: 400,
          height: 300,
          backgroundColor: 'grey',
          borderRadius: 5
        }}>
          <Grid container justifyContent='flex-start' padding={2}>
            <Grid item><SelectVariants /></Grid>
            <Grid item><FirstComponent /></Grid>
            <Grid item><SecondComponent /></Grid>
            <Grid item>
              <Typography variant='h4'>
                {props.pricePerDay} THB
              </Typography>
            </Grid>

          </Grid>

        </Box>
      </Grid>
      <Grid item>
        <Box sx={{
          width: 400,
          height: 600,
          backgroundColor: 'grey',
          borderRadius: 5
        }}>
          <Typography variant="h6" gutterBottom>
            Renter Information
          </Typography>
          <Grid container spacing={3} padding={2}>
            <Grid item xs={12} sm={6}>
              <TextField
                required
                id="firstName"
                name="firstName"
                label="First name"
                fullWidth
                autoComplete="given-name"
                variant="standard"
              />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField
                required
                id="lastName"
                name="lastName"
                label="Last name"
                fullWidth
                autoComplete="family-name"
                variant="standard"
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                required
                id="email"
                name="email"
                label="Email"
                fullWidth
                autoComplete="email"
                variant="standard"
              />
            </Grid>
            
            <Grid item xs={12} sm={6}>
              <TextField
                required
                id="phone-number"
                name="phone-number"
                label="Phone number"
                fullWidth
                autoComplete="phone number"
                variant="standard"
              />
            </Grid>
          </Grid>
        </Box>
      </Grid>
      <Grid item>
        <Box sx={{
          width: 400,
          height: 600,
          backgroundColor: 'grey',
          borderRadius: 5}}>
          <Typography variant="h6" gutterBottom>
            Payment method
          </Typography>
          <Grid container spacing={3}>
            <Grid item xs={12} md={6}>
              <TextField
                required
                id="cardName"
                label="Name on card"
                fullWidth
                autoComplete="cc-name"
                variant="standard"
              />
            </Grid>
            <Grid item xs={12} md={6}>
              <TextField
                required
                id="cardNumber"
                label="Card number"
                fullWidth
                autoComplete="cc-number"
                variant="standard"
              />
            </Grid>
            <Grid item xs={12} md={6}>
              <TextField
                required
                id="expDate"
                label="Expiry date"
                fullWidth
                autoComplete="cc-exp"
                variant="standard"
              />
            </Grid>
            <Grid item xs={12} md={6}>
              <TextField
                required
                id="cvv"
                label="CVV"
                helperText="Last three digits on signature strip"
                fullWidth
                autoComplete="cc-csc"
                variant="standard"
              />
            </Grid>
            <Grid item xs={12}>
              <FormControlLabel
                control={<Checkbox color="secondary" name="saveCard" value="yes" />}
                label="Remember credit card details for next time"
              />
            </Grid>
          </Grid>
        </Box>


      </Grid>

    </Grid>
    <Box display = 'flex' justifyContent='center'>
      <Button variant="contained" size='large' sx={{width:500}}>
        เลือกคันนี้
      </Button>
    </Box>
    

  </div>)
}

export default Car;