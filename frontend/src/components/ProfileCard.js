import React, { useState } from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

function ProfileCard(props) {
  const { name: initialName, surname: initialSurname, sex: initialSex, birthday: initialBirthday, note: initialNote } = props;
  const [name, setName] = useState(initialName);
  const [surname, setSurname] = useState(initialSurname);
  const [sex, setSex] = useState(initialSex);
  const [birthday, setBirthday] = useState(initialBirthday);
  const [note, setNote] = useState(initialNote);
  
  const handleNameChange = (event) => setName(event.target.value);
  const handleSurnameChange = (event) => setSurname(event.target.value);
  const handleSexChange = (event) => setSex(event.target.value);
  const handleBirthdayChange = (event) => setBirthday(event.target.value);
  const handleNoteChange = (event) => setNote(event.target.value);
  const handleSave = () => {
    // Call a function to save the changes
    console.log('Saving changes...');
  };

  return (
    <div className="profile-card-box">
      <div className="profile-card">
        <h2>Profile</h2>
        <div>
          <label htmlFor="name-input">Name:</label>
          <input id="name-input" type="text" value={name} onChange={handleNameChange} />
        </div>
        <div>
          <label htmlFor="surname-input">Surname:</label>
          <input id="surname-input" type="text" value={surname} onChange={handleSurnameChange} />
        </div>
        <div>
          <label htmlFor="sex-input">Sex:</label>
          <input id="sex-input" type="text" value={sex} onChange={handleSexChange} />
        </div>
        <div>
          <label htmlFor="birthday-input">Birthday:</label>
          <input id="birthday-input" type="text" value={birthday} onChange={handleBirthdayChange} />
        </div>
        <div>
          <label htmlFor="note-input">Note:</label>
          <textarea id="note-input" value={note} onChange={handleNoteChange} />
        </div>
        <button onClick={handleSave}>Save Updates</button>
      </div>
    </div>
  );
}

export default ProfileCard;