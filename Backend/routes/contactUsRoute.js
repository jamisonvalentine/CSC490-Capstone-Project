const router = require('express').Router();
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');

router.route('/').post((req, res) => {
    console.log(req.body);
    nodemailer.createTestAccount((err, account) => {
        const htmlEmail = `
        <h4>Contact us form</h4>
        
        <p> Name: ${req.body.name}</p>
        <p> Email: ${req.body.email}</p>
        <p> Message: ${req.body.message}</p>
        
         `

        let transporter = nodemailer.createTransport({
            host: 'smtp.ethereal.email',
            port: 587,
            secure: false, // true for 465, false for other ports
            auth: {
                user: process.env.NODEMAILER_USER,
                pass: process.env.NODEMAILER_PASSWORD
            },
        })
        
        let mailOptions = {
            from: 'Transfer Tool Contact Us Form',
            to: 'nathanial.skiles@ethereal.email', 
            replyTo: req.body.email,
            subject: 'Message from ' + req.body.name + ' via Contact Us form',
            text: req.body.message,
            html: htmlEmail
        }

        transporter.sendMail(mailOptions, (err, info) => {
            if(err) {
                res.json('Error');
                return console.log(err);
            }
            console.log('Message sent');
            res.json('Success');
        })
        
    })
});

module.exports = router;