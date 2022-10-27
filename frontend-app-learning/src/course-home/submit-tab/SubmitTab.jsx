import React , { useState, useEffect } from 'react'
import { useSelector } from 'react-redux';

function SubmitTab() {
  const {
    courseId,
  } = useSelector(state => state.courseHome);

  const url = `http://portal-staging.funix.edu.vn/api/v1/assignment/getAssignmentByInstance/${courseId}`
  const getData = () => {
    fetch(url)
      .then((res) => res.json())
      .then((res) => {
        console.log(res)
      })
  }
  useEffect(() => {
    getData()
  }, [])

  return (
    <>
        <form>
          <label htmlFor="asm">Choose a assignment:</label>
          <select name="asms" id="asms" form="asmform">
            <option value="ASM_1">ASM 1</option>
            <option value="ASM 2">ASM 2</option>
            <option value="ASM 3">ASM 3</option>
            <option value="ASM 4">ASM 4</option>
          </select>
          <br/>
          <label htmlFor="myfile">Select a file:</label>
          <input type="file" id="myfile" name="myfile" />
          <br/>
          <button>Submit Assignment</button>
        </form>
    </>
  );
}

export default SubmitTab;
