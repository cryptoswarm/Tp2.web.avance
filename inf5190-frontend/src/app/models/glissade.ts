export interface Glissade {
  arrondissement_id: number,
  glissade_id: number,
  name: string,
  date_maj?: Date,
  ouvert?: boolean,
  deblaye?: boolean,
  condition?: string
}


// export interface GlissadeForEdit {
//   arrondissement_id: number,
//   name: string,
//   date_maj: string,
//   ouvert: number,
//   deblaye: number,
//   condition: string
// }

export class GlissadeForEdit {
  arrondissement_id: number | undefined;
  name: string | undefined;
  date_maj: string | undefined;
  ouvert: string | undefined;
  deblaye: string | undefined;
  condition: string | undefined;

}

//   arrondissement_id: number,
//   name: string,
//   date_maj: string,
//   ouvert: number,
//   deblaye: number,
//   condition: string
// }
