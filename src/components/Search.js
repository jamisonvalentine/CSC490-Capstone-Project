import React, { useState, useEffect } from 'react'
import Header from './lib/Header';
import Footer from './lib/Footer';
import Dialog from '@material-ui/core/Dialog';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import Button from '@material-ui/core/Button';
import DialogActions from '@material-ui/core/DialogActions';

import MaterialTable from "material-table";
import Find from "@material-ui/icons/Search";
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
import Edit from "@material-ui/icons/Edit";
import Delete from "@material-ui/icons/Delete";

const Search = () => {
    let [selectedCollege, setSelectedCollege] = useState({
        College: ""
    });

    //state variable for keeping track of data saved in local storage
    let [savedTableData, setSavedTableData] = useState(JSON.parse(localStorage.getItem("saveTableData")));

    //state variable for keeping track of what data is loaded onto table
    let [loadingData, setLoadingData] = useState([]);

    //clear table and local storage
    let handleClear = () => {
        setSavedTableData([]);
        localStorage.clear();
    }

    const columns = [
        { title: "Subject", field: "CourseSubject" },
        { title: "Course Number", field: "ClassID" },
        { title: "College", field: "College" },
        { title: "Instructor", field: "Instructor" },
        { title: "Section", field: "SectionNumber" },
        { title: "Dates", field: "Dates" },
        { title: "Location", field: "Location" },
        { title: "Cost", field: "Cost" }
    ];
    //state variable for keeping track of course info dialog
    const [open, setOpen] = useState(false);


    //Set table data once it is retrieved from local storage
    useEffect(() => {
        if (savedTableData == null) {
            console.log("no data");
        }
        else {
            setLoadingData(savedTableData);
        }

    });

    //open dialog
    let handleRowClick = (e, row) => {
        setSelectedCollege(row);
        console.log(row);
        setOpen(true);
    };

    //close dialog
    let handleClose = () => {
        setOpen(false);
    }
    let handleDeleteRow = (row) => {
        if (savedTableData !== null) {
            let savedData = savedTableData;
            console.log(savedTableData);
            let filteredData = savedData.filter((item) => item !== row);
            console.log(filteredData);
            localStorage.setItem("saveTableData", JSON.stringify(filteredData));
            setSavedTableData(JSON.parse(localStorage.getItem("saveTableData")));
        }
    }


    return (
        <>
            <Header />
            <div className="container search-query px-2 px-sm-3">
                <div><MaterialTable
                    title="Saved Courses"
                    data={loadingData}
                    columns={columns}
                    onRowClick={(evt, selectedRow) => handleRowClick(evt, selectedRow)}
                    options={{
                        search: false,
                        filtering: true,
                        paging: true,
                        pageSize: 5,
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
                        Export: SaveAlt,
                        Filter: FilterList,
                        FirstPage: FirstPage,
                        LastPage: LastPage,
                        NextPage: ChevronRight,
                        PreviousPage: ChevronLeft,
                        Search: Find,
                        Remove: Remove,
                        Add: Add,
                        SortArrow: ArrowDownward,
                        Edit: Edit,
                        ViewColumn: ViewColumn,
                        Delete: Delete
                    }}
                    actions={[
                        {
                            icon: Delete,
                            tooltip: 'Remove Class',
                            onClick: (evt, selectedRow) => handleDeleteRow(selectedRow)
                        }
                    ]}
                />
                </div>


                <div className="d-flex mb-5">
                    <button className="btn text-light bg-primary-custom mr-2" onClick={handleClear}>Clear</button>
                </div>

            </div>
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
                </DialogContent>
                <DialogActions>
                    <Button onClick={handleClose} color="primary">
                        Close
                 </Button>
                </DialogActions>
            </Dialog>
            <Footer />

        </>
    );
}

export default Search;