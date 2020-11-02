import React,{useEffect, useState} from 'react';
import Header from './lib/Header';
import Footer from './lib/Footer';
import axios from 'axios'

const About = () => {
    const [college, setCollege] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:3000/cccourse/college')
        .then(res => {
            setCollege(res.data);
        })
        .catch(err => console.log(err))
    },[])

    return (
        <>
            <Header/>

            <div className="container px-2 px-sm-5 py-5">
                <p className="text-center">
                    If you find a course you need, you can sign up at the NC community college offering it and have the credits transferred to your community colege or university. Contact your advisor before you register for courses at another college
                </p>

                <h4 style={{color: 'red'}}>Include CAA information here</h4>

                <h5 className="text-center mb-3 font-weight-bold">List of Community Colleges</h5>


                <div className="community_college_list list-group w-75 mx-auto">
                    {
                        college.length > 0 ? college.map((item,index) => {
                            return(
                                <p className="list-group-item list-group-item-action" key={index}>{item}</p>
                            )
                        } ):
                        (
                            <p>No Colleges Found</p>
                        )
                    }
                </div>
            </div>

            <Footer/>
            
        </>
    );
}

export default About;