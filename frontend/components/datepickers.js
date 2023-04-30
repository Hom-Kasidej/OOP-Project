import * as React from 'react';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import { InputLabel } from '@mui/material';

function FirstComponent() {
  return (
    <LocalizationProvider dateAdapter={AdapterDayjs} >
      <InputLabel sx = {{color : 'white'}}>จาก</InputLabel>
      <DatePicker sx = {{ backgroundColor: 'white'}}>  </DatePicker>
    </LocalizationProvider>
  );
}
function SecondComponent() {
  return (
    <LocalizationProvider dateAdapter={AdapterDayjs}>
      <InputLabel sx = {{color : 'white'}}>จนกระทั่ง</InputLabel>
      <DatePicker sx = {{ backgroundColor: 'white'}}>  </DatePicker>
    </LocalizationProvider>
  );
}

  export {FirstComponent,SecondComponent};