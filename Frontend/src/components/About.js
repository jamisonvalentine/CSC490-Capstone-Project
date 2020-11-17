import React, { useEffect, useState } from 'react';
import Header from './lib/Header';
import Footer from './lib/Footer';
import axios from 'axios'
import Accordion from 'react-bootstrap/Accordion';
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";
import Form from 'react-bootstrap/Form';

const About = () => {
    const [college, setCollege] = useState([]);
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [message, setMessage] = useState('');


    useEffect(() => {
        axios.get('https://uncgtransfer.herokuapp.com/cccourse/college')
            .then(res => {
                setCollege(res.data);
            })
            .catch(err => console.log(err))
    }, [])

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
        if (name === '' || email === '' || message === '') {
            window.confirm('Please fill out all fields before submitting');
            e.preventDefault();
        }
        else {
            console.log('submitted info: ' + name + email + message);
            axios.post('https://uncgtransfer.herokuapp.com/contactUs/', {
                name: name,
                email: email,
                message: message
            }).then(response => {
                if (response.data === 'Success') {
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

    }

    return (
        <>
            <Header />

            <div className="container px-2 px-sm-5 py-5">
                <p>
                    This application was developed to help UNCG students save time and money by helping them find transferrable courses at local community colleges.
                    If you find a course you need you can sign up at that community college's website. Contact your advisor before you register for courses at another college.
                </p>
                <div>
                    <p>The Comprehensive Articulation Agreement (CAA) is a statewide agreement that governs the
                    transfer of credits between NC community colleges and NC public universities. This application was created using courses in the CAA.
                For more information click <a href={"https://www.nccommunitycolleges.edu/academic-programs/college-transferarticulation-agreements/comprehensive-articulation-agreement-caa"}> here</a>
                    </p>
                </div>

                <div>
                    <Accordion>
                    <Card>
                            <Card.Header>
                                <Accordion.Toggle as={Button} variant="link" eventKey="2">
                                    Contact Us
                                </Accordion.Toggle>
                            </Card.Header>
                            <Accordion.Collapse eventKey="2">
                                <Card.Body>
                                    <p>Feel free to contact us if you have any questions, concerns, or comments and we will get back to you as soon as possible.</p>

                                    <Form onSubmit={handleSubmit} style={{ width: '600px' }}>
                                        <Form.Group controlId="nameField">
                                            <Form.Label>Name</Form.Label>
                                            <Form.Control type="name" placeholder="Enter first and last name" onChange={handleNameChange} />
                                        </Form.Group>

                                        <Form.Group controlId="emailField"  >
                                            <Form.Label>Email address</Form.Label>
                                            <Form.Control type="email" placeholder="Enter email" onChange={handleEmailChange} />

                                        </Form.Group >

                                        <Form.Group controlId="messageField" >
                                            <Form.Label>Message</Form.Label>
                                            <Form.Control as="textarea" rows={3} onChange={handleMessageChange} />
                                        </Form.Group>

                                        <Button variant="primary" type="submit">
                                            Submit
                                        </Button>
                                    </Form>
                                </Card.Body>
                            </Accordion.Collapse>
                        </Card>
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
                                                <p className="list-group-item list-group-item-action" key={index + 1}>{item}</p>
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

            <Footer />

        </>
    );
}

export default About;