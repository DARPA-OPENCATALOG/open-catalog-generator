#!/usr/bin/python
import time
def logo():
  return """
<a href="http://www.darpa.mil/"><img style="float: left; margin: 0px 15px 15px 0px;" height=50 src="darpa.png"></a><h2><a href='index.html' class='topheaderlink'>Open Catalog</a></h2>
"""

def catalog_splash_content():
  date = time.strftime("%Y-%m-%d", time.localtime())
  splash = """
<p>Welcome to the DARPA Open Catalog, which contains a curated list of DARPA-sponsored software and peer-reviewed publications. DARPA funds fundamental and applied research in a variety of areas including data science, cyber, anomaly detection, etc., which may lead to experimental results and reusable technology designed to benefit multiple government domains.</p>
<p>The DARPA Open Catalog organizes publically releasable material from DARPA programs. DARPA has an open source strategy to help increase the impact of government investments.</p>
<p>DARPA is interested in building communities around government-funded software and research. If the R&D community shows sufficient interest, DARPA will continue to make available information generated by DARPA programs, including software, publications, data, and experimental results.</p>
<p>The table on this page lists the programs currently participating in the catalog.</p>
<p>The Open Catalog is operating under the purview of the I2O XDATA program. With questions or concerns, please contact the Program Manager:<br>
Dr. Christopher White<br>
<a href='mailto:christopher.white@darpa.mil'>christopher.white@darpa.mil</a></p>
<p>Report a problem: <a href="mailto:opencatalog@darpa.mil">opencatalog@darpa.mil</a></p>
<p>Last updated: """ 
  splash += date + "</p>"
  return splash

def splash_table_header():
  return """
<h2>Current Catalog Programs:</h2>
<table id='splash' class='tablesorter'> 
<thead> 
<tr> 
    <th>DARPA Program</th> 
    <th>Description</th> 
</tr> 
</thead> 
<tbody> 
"""

def splash_table_footer():
  return """
</tbody> 
</table>
<br>
"""

def software_table_header(columns):
  header = "<table id='software' class='tablesorter'>\n <thead>\n <tr>"
  for column in columns:
    header += "<th>%s</th>" % column
  header += "</tr>\n </thead>\n <tbody>"
  return header

def software_table_footer():
  return """
</tbody> 
</table>
<br>
"""

def pubs_table_header():
  return """
<table id='pubs' class='tablesorter'> 
<thead> 
<tr> 
    <th>Team</th> 
    <th>Title</th> 
    <th>Link</th>
</tr> 
</thead> 
<tbody> 
"""

def pubs_table_footer():
  return """
</tbody> 
</table>
<br>
"""

def catalog_page_header(): 
  return """
<html>
<link rel='stylesheet' href='style.css' type='text/css'/>
<script type='text/javascript' src='jquery-latest.js'></script> 
<script type='text/javascript' src='jquery.tablesorter.min.js'></script> 
<script type='text/javascript'>
$(document).ready(function() 
    { 
        $('#software').tablesorter({
		// sort on the first column and second column, order asc 
        	sortList: [[0,0],[1,0]] 
    	}); 
        $('#pubs').tablesorter({
        	sortList: [[0,0],[1,0]] 
    	});
        $('#splash').tablesorter({
		// sort on the first column, order asc 
        	sortList: [[0,0]] 
    	});
    } 
);
function jump(h){
    var url = location.href;
    location.href = "#"+h;
        history.replaceState(null,null,url)
}   
</script>
"""

def catalog_page_footer():
  return """
<br><br><br>
<hr>
<p><a href='http://www.darpa.mil/FOIA.aspx'>FOIA</a> | <a href='http://www.darpa.mil/Privacy_Security_Notice.aspx'>Privacy and Security</a> | 
<a href='http://www.darpa.mil/NoFearAct.aspx'>No Fear Act</a> | <a href='http://www.darpa.mil/External_Link.aspx?url=http://dodcio.defense.gov/DoDSection508/Std_Stmt.aspx'>Accessibility/Section 508</a></p>
</html>
"""
