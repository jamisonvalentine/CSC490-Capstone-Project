import React, { useEffect, useState } from 'react';
import Header from './lib/Header';
import Footer from './lib/Footer';
import axios from 'axios'
import Accordion from 'react-bootstrap/Accordion';
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";

const About = () => {
    const [college, setCollege] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:3000/cccourse/college')
            .then(res => {
                setCollege(res.data);
            })
            .catch(err => console.log(err))
    }, [])

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
            <Footer />

        </>
    );
}

export default About;