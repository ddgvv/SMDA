<?php
	$date   = $_POST['date'];
	$billno = $_POST['billno'];
	$name=$_POST['name'];
	$address=$_POST['address'];
	$duty=$_POST['duty'];
	$amt=$_POST['amt'];
	$riw=$_POST['riw']
	
	
?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title></title>
     <style type="text/css">
        body
        {
            font-family: Arial;
            font-size: 10pt;
        }
        table
        {
            border: 1px solid #ccc;
            border-collapse: collapse;
        }
        table th
        {
            background-color: #F7F7F7;
            color: #333;
            font-weight: bold;
        }
        table th, table td
        {
            padding: 5px;
            border: 1px solid #ccc;
        }
		p.indent
		{ 
			padding-left: 2.5em ;
			font-weight: bold;
		}
		
    </style>
</head>
<body>
     <table id="tblCustomers" cellspacing="0" cellpadding="0">
        <tr>
    <td colspan="2" rowspan="3"><img src="g.png" alt="" border= height=100 width=100></img></td>
    <td colspan="11" rowspan="3"><h1>
			<center> Sree Maruthi Detective Agency<center> </h1>
<center> <h3>SECURITY & LABOUR CONTRACTOR</h3><center> 
<center> <h5>No.24, Gnanaprakasam Nagar, Main Road,</h5><center> 
<center> <h5>Puducherry-605009. CELL: 8428027349</h5><center> </td>
    <td colspan="5">No:<?php echo $billno;?></td>
</tr>
<tr>
    <td colspan="5"><center> Bill<center> </td>
</tr>
<tr>
    <td colspan="5">Date: <?php echo $date; ?></td>
</tr>
<tr>
    <td colspan="18"><b>Mrs. <?php echo $name;?> <p class="indent"><?php echo $address;?>, Puducherry-605009 </p></b></td>
</tr>
<tr>
    <td colspan="2">Sl.No</td>
	<td colspan="11">Particulars</td>
	<td colspan="2">Total Duty</td>
	<td colspan="3">Total Amount</td>
</tr>

<tr>
    <td colspan="2" rowspan="2">1</br></br></br></br></br></br></td>
	<td colspan="11" rowspan="2">
	<p>Security Guard Duty  Jul-2019</p>
	<p>(01-07-2019 to 31-07-2019) 12 Hours  duty</p>
	</br></br></br></br></br></br>
	</td>
	<td colspan="2"><?php echo $duty;?> Duty</br></br></br></br></br></br></td>
	<td colspan="3"><?php echo $amt;?></br></br></br></br></br></br></td>
</tr>

<tr>
    <td colspan="2">Grand Total</td>
	<td colspan="3"><?php echo $amt?></td>
</tr>

<tr>
    <td colspan="18">
	<p align="right"><b>For Sree Maruthi Detective Agency </b></p>
	Rupees in words:<?php echo $riw;?></td>
	
</tr>

    </table>
    <br />
    <input type="button" id="btnExport" value="Export" onclick="Export()" />
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.22/pdfmake.min.js"></script>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/0.4.1/html2canvas.min.js"></script>
    <script type="text/javascript">
        function Export() {
            html2canvas(document.getElementById('tblCustomers'), {
                onrendered: function (canvas) {
                    var data = canvas.toDataURL();
                    var docDefinition = {
                        content: [{
                            image: data,
                            width: 500
                        }]
                    };
                    pdfMake.createPdf(docDefinition).download("Table.pdf");
                }
            });
        }
    </script>
	
</body>



</html>