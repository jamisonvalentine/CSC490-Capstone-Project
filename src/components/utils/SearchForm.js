import React from 'react';
import TagsInput from 'react-tagsinput'
import 'react-tagsinput/react-tagsinput.css'

function SearchForm(props) {

    let {searchQuery ,setSearchQuery, setResultPage} = props;

    let handleChange = e => {
        const {name , value} = e.target;
        setSearchQuery( prevState => ({
            ...prevState,
            [name] : value
        }))
    }

    const onCourseChanged = (value) => {
        setSearchQuery( prevState => ({
            ...prevState,
            id : value
        }))
    }

    const handleSearch = () => {
        if(searchQuery.id.length && searchQuery.year && searchQuery.semester && searchQuery.type){
            setResultPage(1);
        }else{
            setResultPage(0);
        }
    }

    return (
        <>
            <div className="d-flex flex-column justify-content-center align-items-center px-2 px-sm-5">

                <h2 className="text-center font-weight-bold">
                    Search available course from NC community colleges.
                </h2>

                <h5 className="text-center mb-3">Please enter the following information to get start</h5>

                <div className="form-group row w-75">

                    <select name="id_cat" className="col-md-4 form-control mb-3 mb-md-0 border-none" value={searchQuery.selectIdCat} onChange={handleChange}>
                        <option value="courseId">Course ID</option>
                        <option value="uncgId">Uncg ID</option>
                    </select>

                    {/* <label htmlFor="courseId" className="col-md-4 col-form-label">Course ID</label> */}
                    <div className="col-md-8">
                        <TagsInput inputProps={{placeholder : " "}} value={searchQuery.id} onChange={onCourseChanged} />
                        {/* <input className="form-control" id="courseId" name="id" value={searchQuery.id} onChange={handleChange}/> */}
                    </div>
                </div>

                <div className="form-group row w-75">
                    <label htmlFor="academicYear" className="col-md-4 col-form-label">Academic year</label>
                    <div className="col-md-8">
                        <select id="academicYear" name="year" className="form-control" value={searchQuery.year} onChange={handleChange}>
                            <option value="2020">2020</option>
                            <option value="2019">2019</option>
                            <option value="2018">2018</option>
                            <option value="2017">2017</option>
                        </select>
                    </div>
                </div>

                <div className="form-group row w-75">
                    <label htmlFor="semester" className="col-md-4 col-form-label">Semester</label>
                    <div className="col-md-8">
                        <select id="semester" name="semester" className="form-control" value={searchQuery.semester} onChange={handleChange}>
                            <option value="Summer">Summer</option>
                            <option value="Fall">Fall</option>
                            <option value="Winter">Winter</option>
                        </select>
                    </div>
                </div>

                <div className="form-group row w-75">
                    <label htmlFor="courseType" className="col-md-4 col-form-label">Type of course</label>
                    <div className="col-md-8">
                        <select id="courseType" name="type" className="form-control" value={searchQuery.type} onChange={handleChange}>
                            <option value="All">All</option>
                            <option value="Online">Online</option>
                            <option value="Ofline">Ofline</option>
                        </select>
                    </div>
                </div>

                <button className="btn mt-3 bg-primary-custom text-light" onClick = {handleSearch}>Search</button>

                </div>
        </>
    );
}

export default SearchForm;