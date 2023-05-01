import React, { useState } from "react";

function PaymentOptionCard() {
  const [creditCards, setCreditCards] = useState([]);

  function handleAddCard() {
    setCreditCards([...creditCards, { number: "", cvc: "" }]);
  }

  function handleDeleteCard(index) {
    const newCards = [...creditCards];
    newCards.splice(index, 1);
    setCreditCards(newCards);
  }

  function handleChangeCard(event, index, key) {
    const newCards = [...creditCards];
    newCards[index][key] = event.target.value;
    setCreditCards(newCards);
  }

  return (
    <div className="payment-card">
      <h2>Payment Options</h2>
      {creditCards.map((card, index) => (
        <div key={index}>
          <label>Credit Card Number</label>
          <input
            type="text"
            value={card.number}
            placeholder="Enter card number"
            onChange={(event) => handleChangeCard(event, index, "number")}
          />
          <label>CVC</label>
          <input
            type="text"
            value={card.cvc}
            placeholder="Enter CVC"
            onChange={(event) => handleChangeCard(event, index, "cvc")}
          />
          <button onClick={() => handleDeleteCard(index)}>Delete</button>
        </div>
      ))}
      <button onClick={handleAddCard}>Add Card</button>
    </div>
  );
}

export default PaymentOptionCard;
