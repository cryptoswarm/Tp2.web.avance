import { PatinoirCondition } from "./patinoire-conditions";

export interface Patinoire{
  id: number,
  nom_pat: string,
  conditions?: PatinoirCondition[]
}
