#!/usr/bin/perl

# generate_html.pl
# This generates an HTML output from the Make/Model. 
# Uses regex to create output html's.

use strict;
use warnings;
use File::Basename;
use File::Path qw(make_path);

# SPLIT args from command
my %data;
foreach my $arg (@ARGV) {
    my ($key, $value) = split('=', $arg, 2);
    $data{$key} = $value;
}

# CREATE the HTML code
my $html_content = <<HTML;
<html>
<head><title>$data{Make} $data{Model} Information</title></head>
<body>
<h1>$data{Make} $data{Model}</h1>
<table border="1">
<tr><th>Horsepower</th><td>$data{Horsepower}</td></tr>
<tr><th>Torque</th><td>$data{Torque}</td></tr>
<tr><th>Transmission Type</th><td>$data{Transmission_Type}</td></tr>
<tr><th>Drivetrain</th><td>$data{Drivetrain}</td></tr>
<tr><th>Fuel Economy</th><td>$data{Fuel_Economy}</td></tr>
<tr><th>Model Year Range</th><td>$data{Model_Year_Range}</td></tr>
<tr><th>Engine Type</th><td>$data{Engine_Type}</td></tr>
<tr><th>Oil Type</th><td>$data{Oil_Type}</td></tr>
<tr><th>Oil Capacity</th><td>$data{Oil_Capacity}</td></tr>
<tr><th>Open Recalls</th><td>$data{Open_Recalls}</td></tr>
</table>
</body>
</html>
HTML

# Function to get a new filename if the file already exists
sub get_new_filename {
    my ($dir, $base_name, $extension) = @_;
    my $counter = 1;

    while (-e "$dir/$base_name$counter.$extension") {
        $counter++;
    }

    return "$dir/$base_name$counter.$extension";
}

# CHECK for results directory
my $results_dir = "results";
unless (-d $results_dir) {
    make_path($results_dir) or die "Bad path: $results_dir";
}

# CHECK for initial output file
my $filename = "$results_dir/output.html";
if (-e $filename) {
    my ($name, $path, $suffix) = fileparse($filename, qr/\.[^.]*/);
    $filename = get_new_filename($results_dir, $name, substr($suffix, 1)); # substr to remove leading dot in extension
}

# OUTPUT HTML file to the available filename
open(my $fh, '>', $filename) or die "Cannot open $filename: $!";
print $fh $html_content;
close($fh);

print "HTML file generated: $filename\n";
