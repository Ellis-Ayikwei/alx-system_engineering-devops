# Change OS configuration for holberton user
exec { 'change-os-configuration-for-holberton-user':
  command => 'ulimit -n 2048',
  user    => 'root',
}