import { useState } from "react";
import * as XLSX from 'xlsx';
import FileUploader from "./fileupload";
import Data from "./data";
import NotificationComponent from "./noti";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./pages/login";
import AdminHome from "./pages/adminhome";
import StudentHome from "./pages/userhome";
function App() {

  // onchange states
 /* const [excelFile, setExcelFile] = useState(null);
  const [typeError, setTypeError] = useState(null);

  // submit state
  const [excelData, setExcelData] = useState(null);

  // onchange event
  const handleFile=(e)=>{
    let fileTypes = ['application/vnd.ms-excel','application/vnd.openxmlformats-officedocument.spreadsheetml.sheet','text/csv'];
    let selectedFile = e.target.files[0];
    if(selectedFile){
      if(selectedFile&&fileTypes.includes(selectedFile.type)){
        setTypeError(null);
        let reader = new FileReader();
        reader.readAsArrayBuffer(selectedFile);
        reader.onload=(e)=>{
          setExcelFile(e.target.result);
        }
      }
      else{
        setTypeError('Please select only excel file types');
        setExcelFile(null);
      }
    }
    else{
      console.log('Please select your file');
    }
  }
  
  // submit event
  const downloadPdf=()=>{
    window.print()
  }
  const handleFileSubmit=(e)=>{
    e.preventDefault();
    if(excelFile!==null){
      const workbook = XLSX.read(excelFile,{type: 'buffer'});
      const worksheetName = workbook.SheetNames[0];
      const worksheet = workbook.Sheets[worksheetName];
      const data = XLSX.utils.sheet_to_json(worksheet);
      setExcelData(data.slice(0,10));
    }
  }*/
  

  return (
    <>
    <BrowserRouter>
    <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/admin-home" element={<AdminHome />} />
      <Route path="/student-home" element={<StudentHome />} />
    </Routes>
  </BrowserRouter>
<div>
        <iframe title="Diversity_and_inclusion_dashboard" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=7053b9ff-f81f-4c4c-a8e7-8984048dff7c&autoAuth=true&ctid=cca3f0fe-586f-4426-a8bd-b8146307e738" frameborder="0" allowFullScreen="true"></iframe>
      </div>
      <FileUploader/>
      <div className="mt-20">
       <Data/>
      </div>

    </>
  );
}

export default App;
