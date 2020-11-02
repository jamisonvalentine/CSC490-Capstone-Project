import React from 'react';

function SearchResult({searchQuery,setSearchQuery,setResultPage,searchData}) {
    let handleClick = () => {
        setSearchQuery({
            id : '',
            year : '2020',
            semester : 'Fall',
            type : 'Online'
        })

        setResultPage(0);
    }
    return (
        <div className="container search-query px-2 px-sm-3">
            <h5 className="font-weight-bold text-center mb-3">Show search result for:</h5>
            <div className="row">
                <div className="col-6 mb-3 mb-md-0 col-md-3">
                    <p className="text-center">Course id</p>
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

            <div className="search-result-table table-responsive-lg my-4">
                <table className="table">
                    <thead>
                        <tr>
                        <th scope="col">Name of Community college</th>
                        <th scope="col">Course ID</th>
                        <th scope="col">Credit</th>
                        <th scope="col">Course description</th>
                        <th scope="col">Cost</th>
                        </tr>
                    </thead>
                    <tbody>

                    {
                        searchData.length > 0 ? searchData.map (item => {
                            let date = item.Dates.split('-');
                            let year = new Date(date[0]).getFullYear();
                            {/* let sem = item.Semester.split('-'); */}
                            console.log(year)
                            if(year == searchQuery.year /*&& searchQuery.semester == sem[0]*/){
                                return (
                                    <tr key={item._id}>
                                        <th>{item.College}</th>
                                        <td>{searchQuery.id}</td>
                                        <td>{item.Credits}</td>
                                        <td>Course description</td>
                                        <td>$1000</td>
                                    </tr>

                                )
                            }
                        }):
                        (
                            <tr>
                                <th>No result...</th>
                            </tr>
                        )
                    }

                    </tbody>
                </table>
            </div>
            <button className="btn text-light bg-primary-custom" onClick={handleClick}>Reset</button>
        </div>
    );
}

export default SearchResult;