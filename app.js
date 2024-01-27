const express = require('express');
const nodemailer = require('nodemailer');
const app = express();
const port = 3000;

app.use(express.static('public'));

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});

// Configuring nodemailer
const transporter = nodemailer.createTransport({
  service: 'smtp.gmail.com',
  auth: {
    user: 'bitaplus8@gmail.com', // Replace with your Gmail address
    pass: 'cimi pxyb ubdw krin' // Replace with your Gmail password
  }
});

app.post('/send-email', (req, res) => {
  const mailOptions = {
    from: 'bitaplus8@gmail.com', // Replace with your Gmail address
    to: 'productionzpr@gmail.con', // Replace with the recipient's email address
    subject: 'Hello, check out this image!',
    html: '<p>This is the message body.</p> <img src="data:image/png;base64,IMAGE_DATA">'
    // Replace IMAGE_DATA with the actual Base64 image data
  };

  transporter.sendMail(mailOptions, (error, info) => {
    if (error) {
      return console.log(error);
    }
    console.log('Email sent:', info.response);
    res.send('Email sent successfully!');
  });
});