import React from 'react';
import {Link} from 'react-router-dom'

function Footer() {
    return (
        <footer className="py-2 px-3 d-flex flex-column mt-4 mt-sm-0 bg-light">
            <Link to='/' className="text-dark text-center">Contact information</Link>
            <Link to='/' className="text-center text-dark">All right reserved by</Link>
        </footer>
    );
}

export default Footer;