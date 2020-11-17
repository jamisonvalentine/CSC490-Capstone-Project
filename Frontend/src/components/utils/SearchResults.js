import React, { useState, useEffect } from 'react';
import Modal from '../lib/Modal';
import Dialog from '@material-ui/core/Dialog';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import Button from '@material-ui/core/Button';
import DialogActions from '@material-ui/core/DialogActions';
import MaterialTable from "material-table";
import Search from "@material-ui/icons/Search";
import ViewColumn from "@material-ui/icons/ViewColumn";
import SaveAlt from "@material-ui/icons/SaveAlt";
import ChevronLeft from "@material-ui/icons/ChevronLeft";
import ChevronRight from "@material-ui/icons/ChevronRight";
import FirstPage from "@material-ui/icons/FirstPage";
import LastPage from "@material-ui/icons/LastPage";
import Add from "@material-ui/icons/Add";
import Check from "@material-ui/icons/Check";
import FilterList from "@material-ui/icons/FilterList";
import Remove from "@material-ui/icons/Remove";
import ArrowDownward from "@material-ui/icons/ArrowDownward";
import Clear from "@material-ui/icons/Clear";
import DeleteOutline from "@material-ui/icons/DeleteOutline";
import Edit from "@material-ui/icons/Edit";
import More from "@material-ui/icons/More";




function SearchResult({ searchQuery, setSearchQuery, setResultPage, searchData, setSearchData }) {

    let [selectedCollege, setSelectedCollege] = useState({
        College: ""
    });

    //state variable that lets up keep track of course dialog info
    const [open, setOpen] = useState(false);

    const columns = [
        { title: "Subject", field: "CourseSubject" },
        { title: "Course Number", field: "ClassID" },
        { title: "Course Name", field: "CourseName" },
        { title: "College", field: "College" },
        { title: "Section", field: "SectionNumber" },
        { title: "Dates", field: "Dates" },
        { title: "Location", field: "Location" },
        { title: "Cost", field: "Cost" },
        { title: "UNCG ID", field: "UncgID"}
    ];

    //Place holder while table data loads
    const [tableData, setTableData] = useState([
        { CourseSubject: "loading" }
    ]);


    let handleClick = () => {
        setSearchQuery({
            id_cat: 'courseId',
            id: [],
            year: '2020',
            semester: 'Fall',
            type: 'Online'
        })
        setResultPage(0);
        setSearchData(null);
    }

    //save all rows into local storage
    let handleSaveAll = () => {
        let saveResults = localStorage.getItem('saveTableData');
        let saveData = saveResults ? JSON.parse(saveResults).concat(searchData) : [].concat(searchData);
        localStorage.setItem("saveTableData", JSON.stringify(saveData));
        window.alert("Search Result Saved");
    }

    //Set table data once it is loaded from backend
    useEffect(() => {
        if (searchData == null) {
            console.log("not ready");
        }
        else {
            setTableData(searchData);
        }
    });

    let handleRowClick = (e, row) => {
        setSelectedCollege(row);
        setOpen(true);
    };

    //close dialog
    let handleClose = () => {
        setOpen(false);
    };

    //save specified row into local storage
    let handleSaveRow = (row) => {
        let saveResults = localStorage.getItem('saveTableData');
        let saveData = saveResults ? JSON.parse(saveResults).concat(row) : [].concat(row);
        localStorage.setItem("saveTableData", JSON.stringify(saveData));
        window.alert("Search Result Saved");
    };




    return (
        <div className="container search-query px-2 px-sm-3">
            <div className="row">
                <div className="col-6 mb-3 mb-md-0 col-md-3">
                    <p className="text-center">Course ID</p>
                    <input type="text" value={searchQuery.id} className="form-control" readOnly />
                </div>

                <div className="col-6 mb-3 mb-md-0 col-md-3">
                    <p className="text-center">Academic year</p>
                    <input type="text" value={searchQuery.year} className="form-control" readOnly />
                </div>

                <div className="col-6 mb-3 mb-md-0 col-md-3">
                    <p className="text-center">Semester</p>
                    <input type="text" value={searchQuery.semester} className="form-control" readOnly />
                </div>

                <div className="col-6 mb-3 mb-md-0 col-md-3">
                    <p className="text-center">Type of course</p>
                    <input type="text" value={searchQuery.type} className="form-control" readOnly />
                </div>
            </div>

            <div><MaterialTable
                title="Search Results"
                data={tableData}
                columns={columns}
                onRowClick={(evt, selectedRow) => handleRowClick(evt, selectedRow)}
                options={{
                    search: false,
                    filtering: true,
                    paging: true,
                    pageSize: 10,
                    pageSizeOptions: [10, 20, 50],
                    exportButton: true,
                    rowStyle: { height: 5, fontSize: "14px" },
                    headerStyle: { height: 10 },
                    maxBodyHeight: 500
                }}
                icons={{
                    Clear: Clear,
                    Check: Check,
                    DetailPanel: ChevronRight,
                    Delete: DeleteOutline,
                    Export: SaveAlt,
                    Filter: FilterList,
                    FirstPage: FirstPage,
                    LastPage: LastPage,
                    NextPage: ChevronRight,
                    PreviousPage: ChevronLeft,
                    Search: Search,
                    Remove: Remove,
                    Add: Add,
                    SortArrow: ArrowDownward,
                    Edit: Edit,
                    ViewColumn: ViewColumn,
                    More: More
                }}
                actions={[
                    {
                        icon: Add,
                        tooltip: 'Save Class',
                        onClick: (evt, selectedRow) => handleSaveRow(selectedRow)

                    }
                ]}

            />
            </div>


            <div className="d-flex mb-5">
                <button className="btn text-light bg-primary-custom mr-2" onClick={handleClick}>Search Again</button>
                <button className="btn text-light bg-primary-custom mr-2" onClick={handleSaveAll}>Save All</button>
            </div>


            <Modal selectedCollege={selectedCollege} />
            <Dialog
                open={open}
                aria-labelledby="draggable-dialog-title"
            >
                <DialogTitle id="draggable-dialog-title">Course Information</DialogTitle>
                <DialogContent>
                    <DialogContentText>
                        Course Name : {selectedCollege.CourseName}
                    </DialogContentText>
                    <DialogContentText>
                        Class ID : {selectedCollege.ClassID}
                    </DialogContentText>
                    <DialogContentText>
                        Credit Hours : {selectedCollege.Credits}
                    </DialogContentText>
                    <DialogContentText>
                        Instructor : {selectedCollege.Instructor}
                    </DialogContentText>
                    <DialogContentText>
                        Section Number : {selectedCollege.SectionNumber}
                    </DialogContentText>
                    <DialogContentText>
                        Semester : {selectedCollege.Semester}
                    </DialogContentText>
                    <DialogContentText>
                        Year : {selectedCollege.Year}
                    </DialogContentText>
                    <DialogContentText>
                        Class Days : {selectedCollege.ClassDays}
                    </DialogContentText>
                    <DialogContentText>
                        Course Building : {selectedCollege.CourseBuilding}
                    </DialogContentText>
                    <DialogContentText>
                        Course Room : {selectedCollege.CourseRoom}
                    </DialogContentText>
                    <DialogContentText>
                        Location : {selectedCollege.Location}
                    </DialogContentText>
                    <DialogContentText>
                        Time Of Course : {selectedCollege.TimeOfCourse}
                    </DialogContentText>
                    <DialogContentText>
                        Weeks In Semester : {selectedCollege.WeeksInSemester}
                    </DialogContentText>
                    <DialogContentText>
                        Dates : {selectedCollege.Dates}
                    </DialogContentText>
                    <DialogContentText>
                        UNCG ID : {selectedCollege.UncgID}
                    </DialogContentText>
                    <DialogContentText>
                        UNCG Course Title : {selectedCollege.UncgTitle}
                    </DialogContentText>
                </DialogContent>
                <DialogActions>
                    <Button onClick={handleClose} color="primary">
                        Close
                 </Button>
                </DialogActions>
            </Dialog>

        </div>
    );
}

export default SearchResult;