import * as React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import Radio from '@mui/material/Radio';
import Avatar from '@mui/material/Avatar';
import IconButton from '@mui/material/IconButton';
import PhotoCamera from '@mui/icons-material/PhotoCamera';





export default function SimpleContainer() {
    const [name, setName] = React.useState('');
  const [surname, setSurname] = React.useState('');
  const [note, setNote] = React.useState('');
  const [sex, setSex] = React.useState('male');
  const [birthday, setBirthday] = React.useState('');
  const [profileImage, setProfileImage] = React.useState(null);

  const handleImageChange = (event) => {
    setProfileImage(URL.createObjectURL(event.target.files[0]));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(`Name: ${name}, Surname: ${surname}, Note: ${note}, Sex: ${sex}, Birthday: ${birthday}`);
  };

  return (
    <React.Fragment>
      <CssBaseline />
      <Container maxWidth="sm" >
        <Box sx={{ bgcolor: '#cfe8fc', height: 750 , fontSize : '24px', marginBottom: '100px'}}>
          <p>  Profile </p>
          <div style={{ display: 'flex', alignItems: 'center', flexDirection: 'column' }}>
      <Avatar
        src={profileImage}
        sx={{ width: 150, height: 150, margin: '20px' }}
      />
      <input
        accept="image/*"
        id="icon-button-file"
        type="file"
        style={{ display: 'none' }}
        onChange={handleImageChange}
      />
      <label htmlFor="icon-button-file">
        <IconButton color="primary" aria-label="upload picture" component="span">
          <PhotoCamera />
        </IconButton>
      </label>
      <Button variant="contained" disabled={!profileImage}>Save</Button>
    </div>
          <form onSubmit={handleSubmit}>
      <TextField
        label="Name"
        value={name}
        onChange={(event) => setName(event.target.value)}
        fullWidth
        margin="normal"
      />
      <TextField
        label="Surname"
        value={surname}
        onChange={(event) => setSurname(event.target.value)}
        fullWidth
        margin="normal"
      />
      <RadioGroup
        aria-label="Sex"
        name="sex"
        value={sex}
        onChange={(event) => setSex(event.target.value)}
        row
      >
        <FormControlLabel value="male" control={<Radio />} label="Male" />
        <FormControlLabel value="female" control={<Radio />} label="Female" />
      </RadioGroup>
      <TextField
        label="Birthday"
        value={birthday}
        onChange={(event) => setBirthday(event.target.value)}
        fullWidth
        margin="normal"
      />
      <TextField
        label="Note"
        value={note}
        onChange={(event) => setNote(event.target.value)}
        fullWidth
        margin="normal"
        multiline
        rows={4}
      />
      <Button type="submit" variant="contained">Submit</Button>
    </form>
        </Box>
      </Container>
    </React.Fragment>
  );
}
