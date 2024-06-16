# Fix for nginx
exec { 'fix--for-nginx':
  command => 'sed -i "s/worker_processes  1/worker_processes  auto/g" /etc/nginx/nginx.conf',
  user    => 'root',
  notify  => 'Service[nginx]',
}