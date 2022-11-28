export default interface AccountResponse {
  pk: string;
  username: string;
}

export default interface UserInfo {
  id: string;
  username: string;
  email: string;
  firstname: string;
  lastname: string;
  date_of_birth: Date;
  phone: string;
}
