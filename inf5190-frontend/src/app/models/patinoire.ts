import { PatinoirCondition } from "./patinoire-conditions";

export interface Patinoire{
  nom_pat: string,
  conditions: [PatinoirCondition]
}
