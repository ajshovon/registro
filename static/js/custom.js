function doTheInsert() {
    var newRow = document.getElementById('coursesectable').insertRow();
    var select_course_0 = "<td><select name='course[]' id='courses' class='rounded-pill blackborder'><option value='Select Course' selected hidden disabled >Select Course</option>"
    var select_courses_123 = "<option value ='CSE112'>CSE112</option ><option value='MAT111'>MAT111</option><option value='ENG113'>ENG113</option>"
    var select_courses_456 = "<option value ='PHY113'>PHY113</option ><option value='PHY114'>PHY114</option><option value='GED111'>GED111</option></select ></td >"
    var select_Section_0 = "<td><select name='section[]' id='section' class='rounded-pill blackborder'><option value='Select Section' selected hidden disabled >Select Section</option>"
    var select_Section_ABC = "<option value ='A'>A</option ><option value='B'>B</option><option value='C'>C</option>"
    var select_Section_DE = "<option value ='D'>D</option ><option value='E'>E</option></select ></td >"
    newRow.innerHTML = select_course_0 + select_courses_123 + select_courses_456 + select_Section_0 + select_Section_ABC + select_Section_DE;
}

function resetForumInput() {
    document.getElementById("newstdnt").reset();
    document.getElementById("coursesectable").innerHTML = '';
}