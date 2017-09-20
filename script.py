<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html><head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>ERROR: The requested URL could not be retrieved</title>
<style type="text/css"><!-- 
 /*
 * Copyright (C) 1996-2016 The Squid Software Foundation and contributors
 *
 * Squid software is distributed under GPLv2+ license and includes
 * contributions from numerous individuals and organizations.
 * Please see the COPYING and CONTRIBUTORS files for details.
 */

/*
 Stylesheet for Squid Error pages
 Adapted from design by Free CSS Templates
 http://www.freecsstemplates.org
 Released for free under a Creative Commons Attribution 2.5 License
*/

/* Page basics */
* {
	font-family: verdana, sans-serif;
}

html body {
	margin: 0;
	padding: 0;
	background: #efefef;
	font-size: 12px;
	color: #1e1e1e;
}

/* Page displayed title area */
#titles {
	margin-left: 15px;
	padding: 10px;
	padding-left: 100px;
	background: url('/squid-internal-static/icons/SN.png') no-repeat left;
}

/* initial title */
#titles h1 {
	color: #000000;
}
#titles h2 {
	color: #000000;
}

/* special event: FTP success page titles */
#titles ftpsuccess {
	background-color:#00ff00;
	width:100%;
}

/* Page displayed body content area */
#content {
	padding: 10px;
	background: #ffffff;
}

/* General text */
p {
}

/* error brief description */
#error p {
}

/* some data which may have caused the problem */
#data {
}

/* the error message received from the system or other software */
#sysmsg {
}

pre {
    font-family:sans-serif;
}

/* special event: FTP / Gopher directory listing */
#dirmsg {
    font-family: courier;
    color: black;
    font-size: 10pt;
}
#dirlisting {
    margin-left: 2%;
    margin-right: 2%;
}
#dirlisting tr.entry td.icon,td.filename,td.size,td.date {
    border-bottom: groove;
}
#dirlisting td.size {
    width: 50px;
    text-align: right;
    padding-right: 5px;
}

/* horizontal lines */
hr {
	margin: 0;
}

/* page displayed footer area */
#footer {
	font-size: 9px;
	padding-left: 10px;
}


body
:lang(fa) { direction: rtl; font-size: 100%; font-family: Tahoma, Roya, sans-serif; float: right; }
:lang(he) { direction: rtl; float: right; }
 --></style>
</head><body>
<div id="titles">
<h1>ERROR</h1>
<h2>The requested URL could not be retrieved</h2>
</div>
<hr>

<div id="content">
<p>The following error was encountered while trying to retrieve the URL: <a href="http://52.66.129.158/script.py">http://52.66.129.158/script.py</a></p>

<blockquote id="error">
<p><b>Read Error</b></p>
</blockquote>

<p id="sysmsg">The system returned: <i>(104) Connection reset by peer</i></p>

<p>An error condition occurred while reading data from the network. Please retry your request.</p>

<p>Your cache administrator is <a href="mailto:sysadmins@lists.iiit.ac.in?subject=CacheErrorInfo%20-%20ERR_READ_ERROR&amp;body=CacheHost%3A%20proxy%0D%0AErrPage%3A%20ERR_READ_ERROR%0D%0AErr%3A%20(104)%20Connection%20reset%20by%20peer%0D%0ATimeStamp%3A%20Sun,%2023%20Oct%202016%2018%3A18%3A57%20GMT%0D%0A%0D%0AClientIP%3A%2010.2.132.184%0D%0AServerIP%3A%2052.66.129.158%0D%0A%0D%0AHTTP%20Request%3A%0D%0AGET%20%2Fscript.py%20HTTP%2F1.1%0AUser-Agent%3A%20Mozilla%2F5.0%20(X11%3B%20Ubuntu%3B%20Linux%20x86_64%3B%20rv%3A49.0)%20Gecko%2F20100101%20Firefox%2F49.0%0D%0AAccept%3A%20text%2Fhtml,application%2Fxhtml+xml,application%2Fxml%3Bq%3D0.9,*%2F*%3Bq%3D0.8%0D%0AAccept-Language%3A%20en-US,en%3Bq%3D0.5%0D%0AAccept-Encoding%3A%20gzip,%20deflate%0D%0AReferer%3A%20http%3A%2F%2F52.66.129.158%2F%0D%0AConnection%3A%20keep-alive%0D%0APragma%3A%20no-cache%0D%0ACache-Control%3A%20no-cache%0D%0AHost%3A%2052.66.129.158%0D%0A%0D%0A%0D%0A">sysadmins@lists.iiit.ac.in</a>.</p>
<br>
</div>

<hr>
<div id="footer">
<p>Generated Sun, 23 Oct 2016 18:18:57 GMT by proxy (squid/3.5.20)</p>
<!-- ERR_READ_ERROR -->
</div>
</body></html>
