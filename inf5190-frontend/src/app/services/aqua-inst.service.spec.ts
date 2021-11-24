import { TestBed } from '@angular/core/testing';

import { AquaInstService } from './aqua-inst.service';

describe('AquaInstService', () => {
  let service: AquaInstService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AquaInstService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
