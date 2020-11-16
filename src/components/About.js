import React,{useEffect, useState} from 'react';
import Header from './lib/Header';
import Footer from './lib/Footer';
import axios from 'axios'
import Accordion from 'react-bootstrap/Accordion';
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";

const About = () => {
    const [college, setCollege] = useState([]);
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [message, setMessage] = useState('');


    useEffect(() => {
        axios.get('http://localhost:3000/cccourse/college')
        .then(res => {
            setCollege(res.data);
        })
        .catch(err => console.log(err))
    },[])

    const handleNameChange = (e) => {
        setName(e.currentTarget.value);
    }
    const handleEmailChange = (e) => {
        setEmail(e.currentTarget.value);
    }
    const handleMessageChange = (e) => {
        setMessage(e.currentTarget.value);
    }
    const handleSubmit = (e) => {
        console.log('submitted info: ' + name + email + message);
        axios.post('http://localhost:3000/contactUs/', {
            name: name,
            email: email,
            message: message
        }).then(response => {
            if(response.data === 'Success') {
                window.confirm('Message sent');
            }
            else {
                window.confirm('Error has occurred, please retry');
            }
          }).catch((error) => {
            console.log(error);
        });
        
        e.preventDefault();
    }

    return (
        <>
            <Header/>

            <div className="container px-2 px-sm-5 py-5">
                <p className="text-center">
                    If you find a couse you need, you can sign up at the NC community college offering it and have the credits transferred to yout community colege or university. Contact your advisor before you register for courses at another college
                </p>

                <div>
                    <Accordion>
                        <Card>
                            <Card.Header>
                                <Accordion.Toggle as={Button} variant="link" eventKey="0">
                                    Community Colleges Supported
                                </Accordion.Toggle>
                            </Card.Header>
                            <Accordion.Collapse eventKey="0">
                                <Card.Body>
                                    {
                                        college.length > 0 ? college.map((item, index) => {
                                            return (
                                                <p className="list-group-item list-group-item-action" key={index+1}>{item}</p>
                                            )
                                        }) :
                                            (
                                                <p>No Colleges Found</p>
                                            )
                                    }
                                </Card.Body>
                            </Accordion.Collapse>
                        </Card>
                        <Card>
                            <Card.Header>
                                <Accordion.Toggle as={Button} variant="link" eventKey="1">
                                    Cost Calculation Disclaimer
                    </Accordion.Toggle>
                            </Card.Header>
                            <Accordion.Collapse eventKey="1">
                                <Card.Body>In the state of North Carolina, the cost per credit hour of a course taken at a community college is $76. The prices displayed do not
                                take into account miscellaneous prices such as parking, student fees, etc..
                                </Card.Body>
                            </Accordion.Collapse>
                        </Card>
                    </Accordion>
                </div>
            </div>

            <Footer/>
            
        </>
    );
}

export default About;