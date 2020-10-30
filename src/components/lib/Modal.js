import React from 'react';

function Modal({selectedCollege}) {
    return (
        <>
            {selectedCollege && (
                <div className="modal fade" id="exampleModal" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div className="modal-dialog modal-lg" role="document">
                        <div className="modal-content">
                        <div className="modal-header">
                            <h5 className="modal-title" id="exampleModalLabel">{selectedCollege.College}</h5>
                            <button type="button" className="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                        <div className="modal-body">
                            <div className="row">
                                <div className="col-md-6 mb-2">
                                    <p>Course Name : {selectedCollege.CourseName}</p>
                                </div>
                                <div className="col-md-6 mb-2">
                                    <p>Course Subject : {selectedCollege.CourseSubject}</p>
                                </div>
                                <div className="col-md-6 mb-2">
                                    <p>Class ID : {selectedCollege.ClassID}</p>
                                </div>
                                <div className="col-md-6 mb-2">
                                    <p>Credits : {selectedCollege.Credits}</p>
                                </div>
                                <div className="col-md-6 mb-2">
                                    <p>Instructor : {selectedCollege.Instructor}</p>
                                </div>
                                <div className="col-md-6 mb-2">
                                    <p>Section Number : {selectedCollege.SectionNumber}</p>
                                </div>
                                <div className="col-md-6 mb-2">
                                    <p>Semester : {selectedCollege.Semester}</p>
                                </div>
                                <div className="col-md-6 mb-2">
                                    <p>Year : {selectedCollege.Year}</p>
                                </div>
                                <div className="col-md-6 mb-2">
                                    <p>Class Days : {selectedCollege.ClassDays}</p>
                                </div>
                                <div className="col-md-6 mb-2">
                                    <p>Course Building : {selectedCollege.CourseBuilding}</p>
                                </div>
                                <div className="col-md-6 mb-2">
                                    <p>Course Room : {selectedCollege.CourseRoom}</p>
                                </div>
                                <div className="col-md-6 mb-2">
                                    <p>Location : {selectedCollege.Location}</p>
                                </div>
                                <div className="col-md-6 mb-2">
                                    <p>Time Of Course : {selectedCollege.TimeOfCourse}</p>
                                </div>
                                <div className="col-md-6 mb-2">
                                    <p>Weeks In Semester : {selectedCollege.WeeksInSemester}</p>
                                </div>
                                <div className="col-md-6 mb-2">
                                    <p>Dates : {selectedCollege.Dates}</p>
                                </div>
                                
                            </div>
                        </div>
                            {/* <div className="modal-footer">
                                <button type="button" className="btn btn-secondary" data-dismiss="modal">Close</button>
                                <button type="button" className="btn btn-primary">Save changes</button>
                            </div> */}
                        </div>
                    </div>
                </div>

            )}
        </>
    );
}

export default Modal;