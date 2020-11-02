import React,{useRef, useState} from 'react';
import Modal from '../lib/Modal';

function SearchResult({searchQuery,setSearchQuery,setResultPage,searchData,setSearchData}) {
    
    let [selectedCollege, setSelectedCollege] = useState({
        College : ""
    });

    let handleClick = () => {
        setSearchQuery({
            id : '',
            year : '2020',
            semester : 'Fall',
            type : 'Online'
        })
        
        setResultPage(0);
        setSearchData(null);
    }
    
    let handleSave = () => {
        let saveResults = localStorage.getItem('saveResult');
        let saveData = saveResults ? JSON.parse(saveResults).concat(searchData) : searchData;
        localStorage.setItem("saveResult", JSON.stringify(saveData));
        window.alert("Search Result Saved");
        // console.log(JSON.parse(localStorage.getItem("saveResult")))
    }
    
    let tableRef = useRef(null);
    let handlePrint = () => {
        var win = window.open('', '', 'height=700,width=700');
        win.document.write(tableRef.current.outerHTML);
        win.document.close();
        win.print();
    }

    return (
        <div className="container search-query px-2 px-sm-3">
            <h5 className="font-weight-bold text-center mb-3">Show search result for:</h5>
            <div className="row">
                <div className="col-6 mb-3 mb-md-0 col-md-3">
                    <p className="text-center">Course ID</p>
                    <input type="text" value={searchQuery.id} className="form-control" readOnly/>
                </div>

                <div className="col-6 mb-3 mb-md-0 col-md-3">
                    <p className="text-center">Acedemic year</p>
                    <input type="text" value={searchQuery.year} className="form-control" readOnly/>
                </div>

                <div className="col-6 mb-3 mb-md-0 col-md-3">
                    <p className="text-center">Semester</p>
                    <input type="text" value={searchQuery.semester} className="form-control" readOnly/>
                </div>

                <div className="col-6 mb-3 mb-md-0 col-md-3">
                    <p className="text-center">Type of course</p>
                    <input type="text" value={searchQuery.type} className="form-control" readOnly/>
                </div>
            </div>


            
            
            <div className="search-result-table table-responsive-lg my-4" ref={tableRef}>
                <table  className="table">
                    <thead>
                        <tr>
                            <th scope="col">Name of Community College</th>
                            <th scope="col">Course ID</th>
                            <th scope="col">Credit</th>
                            <th scope="col">Course Description</th>
                            <th scope="col">Cost</th>
                        </tr>
                    </thead>
                    <tbody>

                    {
                        searchData && searchData.length > 0 ? searchData.map (item => {
                            return (
                                <tr key={item._id}>
                                    <th>{item.College}</th>
                                    <td>{`${item.CourseSubject} ${item.ClassID}`}</td>
                                    <td>{item.Credits}</td>
                                    <td data-toggle="modal" data-target="#exampleModal" onClick={() => setSelectedCollege(item)}> Click here for more information</td>
                                    <td>${item.Credits * 76}</td>
                                </tr>

                            )
                        }):
                        searchData == null ?
                        (
                            <tr>
                                <td colSpan="5" align="center">
                                    <div className="spinner-border" role="status">
                                        <span className="sr-only">Loading...</span>
                                    </div>
                                </td>
                            </tr>
                        )
                        : 
                        (
                            <tr>
                                <td>No Result Found...</td>
                            </tr>
                        )
                    }

                    </tbody>
                </table>
            </div>
            <div className="d-flex mb-5">
                <button className="btn text-light bg-primary-custom mr-2" onClick={handleClick}>Search Again</button>
                <button className="btn text-light bg-primary-custom mr-2" onClick={handleSave}>Save Result</button>
                <button className="btn text-light bg-primary-custom mr-2" onClick={handlePrint}>Download Pdf</button>
            </div>

           
            <Modal selectedCollege={selectedCollege}/>
        </div>
    );
}

export default SearchResult;