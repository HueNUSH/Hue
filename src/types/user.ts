export class User {
  userId!: string
  username!: string
  createdAt!: number
  email!: string
  isAdmin = false
  userModules!: Array<string>
}
