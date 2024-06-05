file { '/var/www/html/wp-settings.php' :
  ensure => present,
  content => replace(/phpp/g, 'php'),
}
